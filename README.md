# bzCompute

bzCompute is a computation graph library with built-in support for domain-decomposition and prallel computation. The library can be used for expressing and executing large number of mathematical and text-processing operations using Data-Flow graphs, (Educational version of tensorflow), written in pure python code with numpy support.

### Examples :
The educational project supports limited number of text-processing and mathematical operations that are normally used frequently.
**Look at examples folder for various examples**

### Parallel Computation : 
The librabry supports both sequential and parallel computation on graphs. Domain Decomposition is the computation technique used to provide task-level parallelism by creating replicas of computation graphs . The library creates a Master-worker setup, where the MasterSession creates specified number of worker sessions, each worker-session is a thread. These threads can be pre-forked to memory or can be created on demand. Each worker is automatically assigned a name. The results are collected. Domain decomposition is manily used for running multiple replicas of data-flow graphs on different inputs, check out *examples*.

### Supported Sessions : 
The library supports three types of sessions as of now : 

  * **SequentialSession** : SequentialSession executes computation graph in a sequential order, leaving parallelism to OS and Hardware.
  *  **MasterSession** : Creates a master session for parallel computation, can be used for domain-decomposition, by specifying number of worker threads.
  *  **StringSession** : It is a variant of SequentialSession for executing a computation graph composed of strign operations. 
 
### Supported Operations : 
bzCompute supports many operations as of now, the library also provides support for defining custom operations as per the requirements.

##### Numerical Operations :
Look at *pyCompute/KernelOperations.py* to obtain list of all supported operations

#### Text-Processing Operations : 
Look at *pyCompute/text_processing/StringOperations.py* for all supported string operations.

