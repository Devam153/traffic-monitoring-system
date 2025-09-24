# Traffic Monitoring System 🚦

A Python project that calculates adaptive green light durations based on vehicle density from traffic images.

---

## Problem Statement

Traffic congestion is a huge problem in modern cities, causing wasted time, frustration, accidents, and increased pollution.  
Traditional traffic lights often follow fixed timings, which are ineffective during peak hours.

This project analyzes traffic images and suggests **adaptive green light durations** based on vehicle positions and density.

---

## Approach

1. Select a traffic image.
2. Detect all vehicles using **CVLib** and outline them with bounding boxes.
3. Measure the distance of vehicles from the start of the road.
4. Calculate a suitable green light duration based on vehicle count and distance.
5. Save the results to a **MySQL database**.
6. Display the image with bounding boxes and calculated green light duration.

---

## Libraries Used

- `cv2` (OpenCV) – image processing
- `cvlib.object_detection` – vehicle detection
- `matplotlib` – plotting images
- `math` – calculations
- `tabulate` – display results
- `mysql-connector` – store traffic data

---

_Feel free to hit me up if you have any criticism, feedback or ideas for improvement :)_
