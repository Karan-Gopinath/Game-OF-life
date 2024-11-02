Game of Life Simulation

This project implements Conway's Game of Life using Python and Matplotlib. The Game of Life is a cellular automaton created by British mathematician John Conway. It's a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. The cells on the grid will live, die, or reproduce based on a set of rules, creating complex, evolving patterns.
Features

    Configurable grid size
    Adjustable speed for simulation
    Random initial configuration of cells
    Visual representation using Matplotlib

Rules of the Game

The game follows these rules for each cell:

    Underpopulation: A live cell with fewer than two live neighbors dies.
    Survival: A live cell with two or three live neighbors lives on to the next generation.
    Overpopulation: A live cell with more than three live neighbors dies.
    Reproduction: A dead cell with exactly three live neighbors becomes a live cell.

Prerequisites

    Python 3.x
    Matplotlib
