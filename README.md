# Capstone

## Overview

This project presents a novel security framework for the Internet of Medical Things (IoMT) by integrating Physical Unclonable Function (PUF) technology with a Single Node Blockchain (SNBC) architecture. The primary goal is to enhance the security of IoMT systems against evolving cyber threats.

The framework leverages:
- **PUF Technology**: For unique device authentication and secure cryptographic key generation.
- **Single Node Blockchain**: For data integrity and efficient management in a centralized manner.

## Project Structure

The repository contains the following files:

- `__init__.py`: Package initialization file.
- `block.py`: Contains the `Block` class for creating and managing blockchain blocks.
- `blockchain.py`: Implements the `Blockchain` class for simulating the blockchain network.
- `config.py`: Configuration file for setting up various parameters.
- `miner.py`: Defines the `Miner` class for simulating the mining process in the blockchain.
- `networking.py`: Provides classes and methods for simulating network behavior.
- `node.py`: Represents a node in the blockchain network.
- `program.py`: Contains the `Base Program` class for handling node programs.
- `vulnerability_before_puf.xlsx`: Excel file documenting vulnerabilities before the integration of PUF.
