import pandas as pd
file="to_do.csv"

def history():
   history=open(file,"r",)
   ab=history.read()
   if len(ab)==0:
       print("no data found: ")
   else:
       print("showing history")
       data=pd.read_csv(file,header=None)
       print(data)
      
       
def delete_history():
    with open("to_do.csv", "w") as f:
     pass  # Or f.write("") — both will clear it
     print("🗑️ All tasks have been deleted.")
    
def main():
  while True:    
    user=input("enter the work or yes to see remaining works (if you want to delete history type del): ").lower()
    if user=="yes":
        history()
        break
    elif user=="del":
        delete_history()
        break
    else:
        print("your work is save to txt file.")
        here=open(file,"a")
        here.writelines(f"{user}\n")
main()
