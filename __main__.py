from simulator import CPU, memory

if __name__ == "__main__":
    cpu = CPU()

#-----------------------------------------------
    # Execute Program No. 1:
    with open("programa1.txt", "r") as file:
        program = file.read()

        
    print("Executing Program No. 1:")
    cpu.execute_program(program)
    # print(f"Memory:\n {memory}")
#-----------------------------------------------
    # Execute Program No. 2:
    with open("programa2.txt", "r") as file:
        program = file.read()

        
    print("Executing Program No. 2:")
    cpu.execute_program(program)
    # print(f"Memory:\n {memory}")
#-----------------------------------------------
    # Execute Program No. 3:
    with open("programa3.txt", "r") as file:
        program = file.read()

        
    print("Executing Program No. 3:")
    cpu.execute_program(program)
    # print(f"Memory:\n {memory}")
#-----------------------------------------------
    # Execute Program No. 4:
    with open("programa4.txt", "r") as file:
        program = file.read()

        
    print("Executing Program No. 4:")
    cpu.execute_program(program)
    # print(f"Memory:\n {memory}")
#-----------------------------------------------

