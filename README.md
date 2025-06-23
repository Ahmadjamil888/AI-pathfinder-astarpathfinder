# A* Path Finder Web Application

This project is a browser-based implementation of the **A\*** (A-Star) pathfinding algorithm using a grid-based interface. It allows users to visually set a starting point, an endpoint, and obstacles, and then computes the shortest path using the A* algorithm.

The application is built with a **Flask** backend in Python and a **frontend developed using HTML, CSS, and JavaScript**. Communication between the frontend and backend is handled through a REST API.

---

## Features

- Interactive 10×10 grid layout
- Click-to-set interface for:
  - Start node (green)
  - End node (red)
  - Obstacles (black)
- Visual display of the shortest path (yellow)
- Backend implemented in Python using Flask
- Cross-Origin Resource Sharing (CORS) enabled for seamless local development
- Easily extendable and modular architecture

---


---

## Getting Started

### Prerequisites

- Python 3.x
- A modern web browser (e.g., Chrome, Firefox, Edge)

---

### Backend Setup

1. Navigate to the backend directory:

    ```bash
    cd backend
    ```

2. Create and activate a virtual environment:

    **Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    **macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```bash
    pip install flask flask-cors
    ```

4. Start the Flask server:

    ```bash
    python model.py
    ```

    The server will run at: `http://127.0.0.1:5000`

---

### Frontend Setup

1. Navigate to the `frontend/` directory:

    ```bash
    cd ../frontend
    ```

2. Open the `index.html` file in your browser by:
   - Double-clicking the file, or
   - Using the **Live Server** extension in VS Code

---

## Usage

1. Click once to place the **start node** (green).
2. Click again to place the **end node** (red).
3. Continue clicking to place **obstacles** (black cells).
4. Click **"Find Path"** to visualize the computed shortest path.
5. Click **"Reset"** to clear and start over.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Author

Developed by Ahmad jamil — AI and Web Developer  
Contact: shazabjamildhami@gmail.com

