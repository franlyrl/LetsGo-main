-- Flyway Migration Script: V1__Create_initial_tables.sql

CREATE TABLE IF NOT EXISTS users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    enabled BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Índices para mejorar el rendimiento
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);

-- Tabla para roles (si es necesaria en el futuro)
CREATE TABLE IF NOT EXISTS roles (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE
);

-- Tabla de relación muchos a muchos entre usuarios y roles
CREATE TABLE IF NOT EXISTS user_roles (
    user_id BIGINT NOT NULL,
    role_id BIGINT NOT NULL,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);

-- Insertar rol por defecto: USER
INSERT INTO roles (name) VALUES ('USER') ON DUPLICATE KEY UPDATE name = VALUES(name);

-- Usuario administrador por defecto (password será encriptada por Spring Security)
INSERT INTO users (username, password, email, first_name, last_name, enabled)
VALUES 
('admin', '$2a$10$N9qo8uLOck8qFq2nI2cYqOevqj5wKc2Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5Z5', 'admin@example.com', 'Admin', 'User', true)
ON DUPLICATE KEY UPDATE username = VALUES(username);