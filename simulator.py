memory = [None] * 300  # Main memory

class CPU:

    #---------------------------------------------------------------------------------------------------    
    def __init__(self):
        self.registers = { 'UC': None, 'ACC': 0, 'PC':None, 'ICR': None, 'MAR': None, 'MDR': None}
        self.PROGRAM_MEMORY = 150 # Place in memory where the program will be loaded
    #---------------------------------------------------------------------------------------------------



    # MEM: Stores a value into a specific memory address without the participation of the CPU registers:-
    def SET(self, addrs, value): 
        memory[addrs] = value
    #----------------------------------------------------------------------------------------------------
        


    # LOAD: Loads the value from the memory location stored in MAR into the ACCUMULATOR:-----------------
    def LDR(self): 
        self.registers['ACC'] = memory[self.registers['MAR']]
    #----------------------------------------------------------------------------------------------------



    # ADDITION: Adds the value from the memory location stored in MAR to the ACCUMULATOR:---------------
    def ADD(self):
        self.registers['ACC'] += memory[self.registers['MAR']]
    #----------------------------------------------------------------------------------------------------
                


    # INCREMENT: Increases the value in the ACCUMULATOR by 1:
    def INC(self):
        self.registers['ACC'] += 1
    #----------------------------------------------------------------------------------------------------



    # DECREMENT: Drecreases the value in the ACCUMULATOR by 1:
    def DEC(self):
        self.registers['ACC'] -= 1
    #----------------------------------------------------------------------------------------------------



    # STORE: Stores the value in the ACCUMULATOR into the memory at the position stored in MAR:----------
    def STR(self):
        memory[self.registers['MAR']] = self.registers['ACC']
    #----------------------------------------------------------------------------------------------------



    # SHOW: There are multiple display options:----------------------------------------------------------
    def SHW(self, target):
        """
        Displays various values depending on the target parameter.

        target: Specifies the register or memory location to display.
        """
                
        if target == 'ACC':
            print(f"ACC: {self.registers['ACC']}")

        
        elif target == 'ICR':
            print(f"ICR: {self.registers['ICR']}")


        elif target == 'MAR':
            print(f"MAR: {self.registers['MAR']}")


        elif target == 'MDR':
            print(f"MDR: {self.registers['MDR']}")


        elif target == 'UC':
            print(f"UC: {self.registers['UC']}")


        else:
            try:
                target = int(target[1:])
                print(f"D{target}: {memory[target]}")
            except ValueError:
                print("Invalid target")
    #----------------------------------------------------------------------------------------------------



    def execute_program(self, program):#----------------------------------------------------------------

        # Load the program into memory:----------------
        instructions = program.split('\n')
        memory[self.PROGRAM_MEMORY:] = instructions                   
        #----------------------------------------------


        print("***********************************************")
        print("Program initialized:")
            
        
        self.registers['PC'] = self.PROGRAM_MEMORY # Program Counter initialized where the first instruction is located in memory
        self.registers['MAR'] = self.registers['PC'] # PC -> MAR


        while(memory[self.registers['MAR']].split()[0] not in ['END', 'PAUSE']):

            self.registers['MDR'] = memory[self.registers['MAR']] # Content in memory of the address MAR -> MDR
            self.registers['ICR'] = self.registers['MDR'] # MDR -> ICR

            self.registers['PC'] += 1                    #  Program Counter + 1
            self.registers['UC'] = self.registers['ICR'] # ICR -> UC
                

            op =  self.registers['UC'].split()[0] # Lets see the operation to know how to continue

            if(op == 'SET'): 
                addrs = int(self.registers['UC'].split()[1][1:])
                value = int(self.registers['UC'].split()[2])
                self.SET(addrs,value)
                

            if(op == 'LDR'): 
                self.registers['MAR'] = int(self.registers['UC'].split()[1][1:])
                self.LDR()
                

            if(op == 'SHW'):
                self.SHW(self.registers['UC'].split()[1])


            if(op == 'ADD'):
                if(self.registers['UC'].split()[2] == 'NULL'):
                    self.registers['MAR'] = int(self.registers['UC'].split()[1][1:])
                    self.ADD()
                    
                elif(self.registers['UC'].split()[3] == 'NULL'):
                    self.registers['MAR'] = int(self.registers['UC'].split()[1][1:])
                    self.registers['ACC'] = memory[self.registers['MAR']]
                    self.registers['MAR'] = int(self.registers['UC'].split()[2][1:])
                    self.ADD()
                    
                else:
                    self.registers['MAR'] = int(self.registers['UC'].split()[1][1:])
                    self.registers['ACC'] = memory[self.registers['MAR']]
                    self.registers['MAR'] = int(self.registers['UC'].split()[2][1:])
                    self.ADD()
                    memory[int(self.registers['UC'].split()[3][1:])] = self.registers['ACC']
                

            if(op == 'INC'):
               self.registers['MAR'] = int(self.registers['UC'].split()[1][1:])
               self.registers['ACC'] = memory[self.registers['MAR']]
               self.INC()


            if(op == 'DEC'):
                self.registers['MAR'] = int(self.registers['UC'].split()[1][1:])
                self.registers['ACC'] = memory[self.registers['MAR']]
                self.DEC()
                

            if(op == 'STR'):
                self.registers['MAR'] = int(self.registers['UC'].split()[1][1:])
                self.STR()

                
            self.registers['MAR'] = self.registers['PC']
                                       
            
        print("Program finalized.")
        print("***********************************************\n")
        
    #----------------------------------------------------------------------------------------------------