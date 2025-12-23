"""
Booking System - Database and Reservation Management
"""

import sqlite3
from datetime import datetime, timedelta
import pandas as pd
from config import DB_NAME, MAX_PARTY_SIZE, MIN_PARTY_SIZE

class BookingSystem:
    def __init__(self):
        self.db_name = DB_NAME
        self.init_database()
    
    def init_database(self):
        """Initialize the bookings database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                party_size INTEGER NOT NULL,
                special_requests TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'confirmed'
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_booking(self, customer_name, email, phone, date, time, party_size, special_requests=""):
        """Create a new booking"""
        # Validate party size
        if party_size < MIN_PARTY_SIZE or party_size > MAX_PARTY_SIZE:
            return {
                "success": False,
                "message": f"Party size must be between {MIN_PARTY_SIZE} and {MAX_PARTY_SIZE} guests."
            }
        
        # Check availability
        if not self.check_availability(date, time, party_size):
            return {
                "success": False,
                "message": "Sorry, this time slot is not available. Please choose another time."
            }
        
        # Create booking
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO bookings (customer_name, email, phone, date, time, party_size, special_requests)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (customer_name, email, phone, date, time, party_size, special_requests))
        
        booking_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return {
            "success": True,
            "booking_id": booking_id,
            "message": f"Booking confirmed! Your reservation ID is {booking_id}."
        }
    
    def check_availability(self, date, time, party_size):
        """Check if a time slot is available"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT SUM(party_size) FROM bookings
            WHERE date = ? AND time = ? AND status = 'confirmed'
        ''', (date, time))
        
        result = cursor.fetchone()
        conn.close()
        
        current_bookings = result[0] if result[0] else 0
        
        # Assuming restaurant capacity of 100 (from config)
        from config import RESTAURANT_INFO
        capacity = RESTAURANT_INFO.get('capacity', 100)
        
        return (current_bookings + party_size) <= capacity
    
    def get_booking(self, booking_id):
        """Retrieve a booking by ID"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM bookings WHERE id = ?', (booking_id,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {
                "id": result[0],
                "customer_name": result[1],
                "email": result[2],
                "phone": result[3],
                "date": result[4],
                "time": result[5],
                "party_size": result[6],
                "special_requests": result[7],
                "created_at": result[8],
                "status": result[9]
            }
        return None
    
    def get_bookings_by_email(self, email):
        """Get all bookings for an email"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM bookings WHERE email = ? ORDER BY date DESC, time DESC', (email,))
        results = cursor.fetchall()
        conn.close()
        
        bookings = []
        for result in results:
            bookings.append({
                "id": result[0],
                "customer_name": result[1],
                "email": result[2],
                "phone": result[3],
                "date": result[4],
                "time": result[5],
                "party_size": result[6],
                "special_requests": result[7],
                "created_at": result[8],
                "status": result[9]
            })
        
        return bookings
    
    def cancel_booking(self, booking_id):
        """Cancel a booking"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('UPDATE bookings SET status = ? WHERE id = ?', ('cancelled', booking_id))
        
        if cursor.rowcount > 0:
            conn.commit()
            conn.close()
            return {"success": True, "message": f"Booking {booking_id} has been cancelled."}
        
        conn.close()
        return {"success": False, "message": "Booking not found."}
    
    def get_all_bookings(self, date=None):
        """Get all bookings, optionally filtered by date"""
        conn = sqlite3.connect(self.db_name)
        
        if date:
            query = 'SELECT * FROM bookings WHERE date = ? ORDER BY time'
            df = pd.read_sql_query(query, conn, params=(date,))
        else:
            query = 'SELECT * FROM bookings ORDER BY date DESC, time DESC LIMIT 100'
            df = pd.read_sql_query(query, conn)
        
        conn.close()
        return df
    
    def get_available_slots(self, date):
        """Get available time slots for a date"""
        from config import BOOKING_SLOTS, RESTAURANT_INFO
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT time, SUM(party_size) as total_guests
            FROM bookings
            WHERE date = ? AND status = 'confirmed'
            GROUP BY time
        ''', (date,))
        
        booked_slots = {row[0]: row[1] for row in cursor.fetchall()}
        conn.close()
        
        capacity = RESTAURANT_INFO.get('capacity', 100)
        available_slots = []
        
        for slot in BOOKING_SLOTS:
            current_bookings = booked_slots.get(slot, 0)
            remaining_capacity = capacity - current_bookings
            
            if remaining_capacity > 0:
                available_slots.append({
                    "time": slot,
                    "available_seats": remaining_capacity
                })
        
        return available_slots
