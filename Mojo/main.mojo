let hello = "Hello World"
# *
#!
#?
# TODO: 
# @param myparam

# * Data types in MOJO
#? string, integer,bool, float, uint

fn main():
    let x: String = "beep1"
    let y: Int = 3
    let z: Int8 = 60 #! Int8 means it takes 8 bits of memory for variable z 
    #! available combinations are Int8, In16, Int32, Int64
    #! Int8, for example, will store numbers between 0 to 255 and so on..
    #! Int wil be default Int64
    
    print(x)
    print(y)
    print(z)