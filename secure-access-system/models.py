from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import bcrypt


db = SQLAlchemy()


# =========================
# User Model
# =========================
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    role = db.Column(db.String(20), nullable=False)
    # role values: resident, concierge, management

    password_hash = db.Column(db.String(255), nullable=False)

    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 🔐 Hash and store password
    def set_password(self, password):
        hashed = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )
        self.password_hash = hashed.decode('utf-8')

    # 🔍 Verify password during login
    def check_password(self, password):
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password_hash.encode('utf-8')
        )

    def __repr__(self):
        return f"<User {self.email} ({self.role})>"
# =========================
# Access Zone Model
# =========================
class AccessZone(db.Model):
    __tablename__ = "access_zones"

    id = db.Column(db.Integer, primary_key=True)
    zone_name = db.Column(db.String(100), nullable=False)
    zone_type = db.Column(db.String(20), nullable=False)
    # private | common

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    access_logs = db.relationship("AccessLog", backref="zone", lazy=True)

    def __repr__(self):
        return f"<AccessZone {self.zone_name} ({self.zone_type})>"


# =========================
# Virtual Key Model
# =========================
class VirtualKey(db.Model):
    __tablename__ = "virtual_keys"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    encrypted_key = db.Column(db.Text, nullable=False)

    is_revoked = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<VirtualKey user_id={self.user_id} revoked={self.is_revoked}>"


# =========================
# Access Log Model (AUDIT TRAIL)
# =========================
class AccessLog(db.Model):
    __tablename__ = "access_logs"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    zone_id = db.Column(db.Integer, db.ForeignKey("access_zones.id"), nullable=False)

    result = db.Column(db.String(10), nullable=False)
    # ALLOW | DENY

    reason = db.Column(db.String(255), nullable=False)

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<AccessLog user={self.user_id} zone={self.zone_id} {self.result}>"
