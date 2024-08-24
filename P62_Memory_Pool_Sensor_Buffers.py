# File: main.py
# Author: Armstrong Subero
# Platform: Raspberry Pi Pico (RP2040) with MicroPython
# Program: P62_Memory_Pool_Sensor_Buffers
# Interpreter: MicroPython (latest version)
# Program Version: 1.0
#
# Program Description: This program demonstrates using a memory pool to manage
#                      memory for sensor data buffers. The memory pool is used
#                      to allocate and deallocate fixed-size memory blocks
#                      efficiently in a memory-constrained environment.
# 
# Hardware Description: No hardware required for this example.
#                       
# Created: August 25th, 2024, 1:30 AM
# Last Updated: August 25th, 2024, 1:30 AM

class MemoryPool:
    def __init__(self, block_size, block_count):
        self.block_size = block_size
        self.pool = bytearray(block_size * block_count)
        self.available_blocks = list(range(block_count))

    def allocate(self):
        if not self.available_blocks:
            raise MemoryError("Out of memory")
        block_index = self.available_blocks.pop()
        start = block_index * self.block_size
        return memoryview(self.pool)[start:start + self.block_size], block_index

    def deallocate(self, block_index):
        self.available_blocks.append(block_index)

# SensorDataBuffer using the MemoryPool
class SensorDataBuffer:
    def __init__(self, memory_pool):
        self.memory_pool = memory_pool
        self.buffer, self.block_index = memory_pool.allocate()
        print(f"Buffer allocated at block index {self.block_index}")

    def write_data(self, data):
        # Assume data is bytes or bytearray and fits within the block size
        self.buffer[:len(data)] = data

    def read_data(self):
        return bytes(self.buffer)

    def release(self):
        print(f"Releasing buffer at block index {self.block_index}")
        self.memory_pool.deallocate(self.block_index)

# Usage example
pool = MemoryPool(32, 10)  # Pool with 10 blocks of 32 bytes each

# Simulating sensor data buffers
buffers = []
try:
    for i in range(5):
        buffer = SensorDataBuffer(pool)
        buffer.write_data(f"SensorData{i}".encode('utf-8'))
        print(f"Buffer {i} contains: {buffer.read_data().decode('utf-8')}")
        buffers.append(buffer)

    # Release some buffers
    buffers[1].release()
    buffers[3].release()

    # Allocate new buffers after releasing
    new_buffer = SensorDataBuffer(pool)
    new_buffer.write_data("NewData".encode('utf-8'))
    print(f"New buffer contains: {new_buffer.read_data().decode('utf-8')}")

finally:
    # Ensure all buffers are released properly
    for buffer in buffers:
        buffer.release()
