# Python TCP Client-Server with PostgreSQL

A simple Python application demonstrating **TCP client-server communication** with **persistent storage in PostgreSQL**.  
The client sends messages to the server, which stores them in a database. This project illustrates **networking, database integration, and backend fundamentals**.


## Features

- TCP-based communication between client and server
- Server stores received messages in PostgreSQL
- Messages include a timestamp (`received_at`)
- Easy-to-run Python scripts
- Works on Windows, Linux, and macOS

## Folder Structure
tcp_server-client/
│
├── tcp_server.py # Server: listens for clients & stores data in DB
├── tcp_client.py # Client: sends messages to server
├── README.md # Project documentation

## Requirements
- Python 3.x
- PostgreSQL 18.x (or any recent version)
- Python library: `psycopg2-binary`

Install dependencies:
pip install psycopg2-binary

##PostgreSQL Setup

1.) Start PostgreSQL service.

2.) Open PostgreSQL shell:  
    psql -U postgres
    
Create database and table:

CREATE DATABASE tcp_app;
\c tcp_app;

CREATE TABLE received_data (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

How to Run:

1️.) Start the TCP Server

Open a terminal and navigate to the project folder:

cd tcp_server-client
python tcp_server.py

You should see:
Server file started
TCP Server listening on 127.0.0.1:5000

Keep this terminal open — the server must run continuously.

2️.) Run the TCP Client

Open another terminal in the same folder:
python tcp_client.py

Expected output:
Server response: Data stored successfully

3️.) Verify Data in PostgreSQL

Open PostgreSQL shell:

psql -U postgres
\c tcp_app
SELECT * FROM received_data;

Expected output:

 id |        message         |      received_at
----+------------------------+----------------------------
  1 | Hello from TCP client! | 2026-01-02 12:30:00
