# 🎬 YouTube Clone

[![GitHub stars](https://img.shields.io/github/stars/Tchakeu/youtube-clone)](https://github.com/Tchakeu/youtube-clone/stargazers)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![Node.js Version](https://img.shields.io/badge/node.js-18.x-green.svg)](https://nodejs.org)

## 📝 Overview

**YouTube Clone** is a full-stack web application that replicates core functionalities of the popular video-sharing platform. Built with **Django** for the backend API and content management, **Express.js** for real-time services, and a responsive frontend to deliver a seamless video streaming experience.

> 🚧 **Note:** This project is currently in active development. Initial structure has been set up with Django, Express.js, and frontend integration.

## ✨ Key Features (Planned/In Progress)

- 🔐 **User Authentication** (JWT-based) – handled by Django REST Framework & `authy` module
- 📹 **Video Upload & Streaming** – chunked uploads, HLS support
- 👍 **Like / Dislike & Comments System** – real-time updates via Express.js
- 🔍 **Search & Recommendations** – full-text search, personalized feeds
- 📁 **User Profiles & Subscriptions** – `profiles` app for user channels
- 🏠 **Home Feed** – dynamic content from the `home` module

## 🛠️ Tech Stack

youtube-clone/
├── manage.py # Django entry point
├── server.js # Express.js server
├── package.json # Node.js dependencies
├── .gitignore
├── Youtube/ # Django project settings (main config)
├── home/ # Home app: feeds, video listing
├── authy/ # Authentication logic
├── profiles/ # User profiles, channels, subscriptions
├── static/ # Frontend assets (CSS, JS, images)
└── README.md


## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18.x + npm
- PostgreSQL (optional, SQLite works for dev)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tchakeu/youtube-clone.git
   cd youtube-clone

   

| Layer       | Technology                                                                 |
|-------------|----------------------------------------------------------------------------|
| Backend API | ![Django](https://img.shields.io/badge/Django-092E20?logo=django) + DRF   |
| Real-time   | ![Express.js](https://img.shields.io/badge/Express.js-000000?logo=express) |
| Database    | PostgreSQL (default) / SQLite for dev                                      |
| Frontend    | HTML5, CSS3, JavaScript (vanilla, located in `static/`)                   |
| Auth        | JWT (Django REST Framework JWT) + `authy` module                          |

## 📂 Project Structure
