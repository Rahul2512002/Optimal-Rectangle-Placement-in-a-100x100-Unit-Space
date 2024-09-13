# Optimal Rectangle Placement in 100x100 Unit Space

## Problem Statement

You are required to choose **five rectangles** of random width and height and place them in a **100x100 unit** space. The placement must be done **optimally** to ensure the total solution area is minimal.

### Rules:
1. Rectangles cannot overlap and must have a **separation of one unit** between them.
2. Rectangles **can be rotated** (width and height swapped) to fit into the space.
3. **No sorting** of rectangles beforehand is allowed.
4. If placement is not possible, an error should be generated.
5. Use **Python** to solve the problem.
6. The **results** should include a plot that shows the rectangle's dimensions (width and height) along with any rotation and its position in the 100x100 unit space.

## Algorithm

The solution follows a **Recursive Partitioning (Divide and Conquer)** strategy:
1. The 100x100 unit space is **divided** into smaller regions.
2. Each subregion is recursively divided until an appropriate place for each rectangle is found.
3. Rectangles are placed while ensuring that no overlap occurs, and each rectangle has a one-unit separation from others.
4. If a rectangle does not fit in the current orientation, it is **rotated** to check for fit.
5. If no valid placement is found, an error is raised.

## Solution Overview

- The algorithm attempts to place the rectangles in the available space by:
  - Checking whether a rectangle can fit in a given subregion.
  - Rotating the rectangle if necessary.
  - Recursively dividing the remaining space to place the next rectangle.

- The **matplotlib** library is used to visualize the solution and generate a plot of the rectangles placed in the 100x100 unit space.

## Code Explanation

### `Rectangle` Class

The `Rectangle` class represents each rectangle with:
- `width` and `height`.
- A method to **rotate** the rectangle, swapping its dimensions.

### `place_rectangles` Function

The main recursive function:
- Tries to place the first rectangle in the available region.
- Recursively divides the remaining space for the remaining rectangles.
- Returns the list of placed rectangles with their positions and rotations.

### `plot_rectangles` Function

This function visualizes the rectangles on a **100x100 grid** using `matplotlib`:
- It ensures that all rectangles are displayed with their correct dimensions, separation, and rotations.

## Installation and Requirements

### Prerequisites

Make sure you have Python installed along with the following required libraries:

```bash
pip install matplotlib
