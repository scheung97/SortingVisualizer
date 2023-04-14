import matplotlib.pyplot as plt
import random
import time

"""Bubble Sort without Red Highlight"""
# def bubble_sort(data):
#     # Perform bubble sort
#     for i in range(len(data)):
#         for j in range(len(data) - 1 - i):
#             if data[j] > data[j + 1]:
#                 data[j], data[j + 1] = data[j + 1], data[j]
#                 # Update chart
#                 plt.clf()
#                 plt.bar(range(len(data)), data)
#                 plt.pause(0.05)

def bubble_sort(data):
    # Perform bubble sort
    for i in range(len(data)):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                # Highlight current swap in red
                plt.clf()
                colors = ['blue'] * len(data)
                colors[j] = 'red'
                colors[j + 1] = 'red'
                plt.bar(range(len(data)), data, color=colors)
                plt.pause(0.05)

                # Swap elements
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def visualize_sort(data):
    # Create chart
    plt.bar(range(len(data)), data)
    plt.draw()
    plt.pause(1)

    # Sort data
    sorted_data = bubble_sort(data)

    # Display sorted data
    plt.clf()
    plt.bar(range(len(sorted_data)), sorted_data)
    plt.draw()
    plt.pause(1)

if __name__ == "__main__":
    # Generate random data
    data = [random.randint(1, 100) for i in range(10)]
    print("Input Data:", data)

    # Visualize sort
    visualize_sort(data)