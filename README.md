# RP2040 Projects by Armstrong Subero

Projects in MicroPython and on the Rasbperry Pi Pico (RP2040).
P stands for Pure Python projects, to complete these you don't need anything except a few LEDs and for many of them
you only need the Pico alone or an RP2040 with a serial connection. 

S are System-level projects. These projects might involve low-level programming, interacting directly with hardware, 
or integrating with operating systems.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Projects](#projects)
  - [P00 to P62 and S01 to S50 Projects](#p00-to-p62-and-s01-to-s50-projects)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains a variety of projects that use the Raspberry Pi Pico (RP2040) microcontroller board. The projects serve as examples of what can be achieved using the RP2040 and include introductory programs like blinking an LED to more advanced topics such as round-robin scheduling, distance measurement, PID loops etc.

## Requirements

To get started, you will need:

- A Raspberry Pi Pico (RP2040) board
- A computer with USB connectivity
- MicroPython installed on Pico
- A USB cable to connect your Pico to the computer

Refer to the [official Raspberry Pi documentation](https://www.raspberrypi.com/documentation/microcontrollers/) for instructions on how to install MicroPython.

## Projects
These projects cover a host of topics from basic to advanced topics. 

### P00 to P62 and S01 to S50 Projects

These projects cover various topics, including mathematical operations, sorting algorithms, design patterns, data structures, control systems, machine learning, and embedded systems programming.

**Files**:
- **P00_Average.py**: Calculates the average of a list of numbers.
- **P01_Looping.py**: Demonstrates different looping techniques.
- **P02_Math.py**: Performs various mathematical operations.
- **P03_Conversion.py**: Demonstrates type conversion in Python.
- **P04_Functions.py**: Shows the use of functions.
- **P06_Formatted_Output.py**: Demonstrates formatted output.
- **P07_Trignometry.py**: Basic trigonometric calculations.
- **P08_Trig_Functions.py**: Advanced trigonometric functions.
- **P09_Resistor_Calculator.py**: Calculates resistor values.
- **P10_Reverse_Words.py**: Reverses words in a sentence.
- **P11_Random.py**: Demonstrates the use of random functions.
- **P12_Sorting.py**: Demonstrates sorting algorithms.
- **P13_File_Operations.py**: Shows file operations.
- **P14_Casting.py**: Demonstrates type casting.
- **P15_Matrix_Addition.py**: Adds two matrices.
- **P16_Class.py**: Basic class example.
- **P17_Dual_Core_Class.py**: Demonstrates dual-core usage with classes.
- **P18_Inheritence.py**: Demonstrates inheritance in OOP.
- **P19_Encapsulation.py**: Demonstrates encapsulation.
- **P20_Polymorphism.py**: Demonstrates polymorphism.
- **P21_Abstraction.py**: Demonstrates abstraction.
- **P22_Composition.py**: Demonstrates composition.
- **P23_Aggregation.py**: Demonstrates aggregation.
- **P24_Singleton.py**: Implements a singleton pattern.
- **P25_Observer.py**: Implements an observer pattern.
- **P26_Factory.py**: Implements a factory pattern.
- **P27_Stratergy_Pattern.py**: Implements a strategy pattern.
- **P28_Command_Pattern.py**: Implements a command pattern.
- **P29_State_Pattern.py**: Implements a state pattern.
- **Sorting algorithms**: `P30_Bubble_Sort.py`, `P31_Selection_Sort.py`, `P32_Insertion_Sort.py`, `P33_Heap_Sort.py`, `P34_Merge_Sort.py`, `P35_Quick_Sort.py`, `P36_Radix_Sort.py`, `P37_Bucketsort.py`
- **Data structures**: `P38_List.py`, `P39_Array.py`, `P40_Stack.py`, `P41_Queue.py`, `P42_Hash_Table.py`, `P43_Dictionary.py`, `P44_BuiltInDataStructures.py`, `P45_Heap.py`, `P46_PriorityQueue.py`, `P47_BinaryTree.py`, `P48_BinarySearchTree.py`, `P49_RedBlackTree.py`, `P50_Trie.py`
- **Caching and control systems**: `P51_LRU_Cache.py`, `P52_Decision_Tree.py`, `P53_Behavior_Tree.py`, `P54_State_Machine.py`, `P55_PID_Loop.py`, `P56_MPC.py`, `P57_MPC_MultiVariableControl.py`, `P58_A_Star.py`, `P59_A_Star.py`, `P60_K_Means.py`
- **Memory and loading**: `P61_Lazy_Loading.py`, `P62_Memory_Pool_Sensor_Buffers.py`
- **Embedded systems**: `S01_Blink.py`, `S02_External_LED.py`, `S03_Timer.py`, `S04_Interrupt.py`, `S05_RGB_LED.py`, `S06_Rotating_LED.py`, `S08_Data_Logger.py`, `S09_PWM.py`, `S10_Fading_Led.py`, `S11_UART.py`, `S15_Dual_Cores.py`, `S16_Different_Blink_Rates.py`, `S17_Sharing_Data.py`, `S18_RTC.py`, `S19_Traffic_Light_Simulation.py`, `S20_Inline_Assembly.py`, `S21_Unique_Identifier.py`, `S22_Light_Dependent_Resistor.py`, `S23_Pot_Brightness_Control.py`, `S24_Simple_Buzzer_Alarm.py`, `S25_Melodies_Player.py`, `S30_Round_Robin_Scheduling.py`, `S31_Emergency_Buffer.py`, `S32_Cooperative_Multitasking.py`, `S33_Mailbox_Queues.py`, `S34_Task_Groups.py`, `S35_Task_Prioritzation.py`, `S36_Event_Semaphones.py`, `S37_Task_Management_System.py`, `S50_HCSR04.py`

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ArmstrongSubero/RP2040.git
   ```

2. Connect your Raspberry Pi Pico to your computer via USB.

3. Upload the desired project to the Pico using a tool such as Thonny (for MicroPython) or using `picotool` if using the C/C++ SDK.

## Contributing

Contributions are welcome! If you'd like to add your own RP2040 projects or improve the existing ones, please fork the repository and submit a pull request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any questions or discussions related to PIC16 Projects:
- **GitHub**: [ArmstrongSubero](https://github.com/ArmstrongSubero)
- **Email**: [armstrong.subero@example.com](mailto:armstrong.subero@gmail.com)

If you find this repository helpful, please give it a star ⭐ and share it with others who might be interested in PIC16 microcontroller projects!
