import os
import time




def main():
 
    
  def data_validation(string):
      if len(string) > 40:
        print("invalid input!")
        exit()
      
  
 
  need_validation = ("-")
  num_of_tries = 0
  # give user three tries to get name format correct
  while num_of_tries < 3:
    project_name = input("What is the name of this project? (need '-' and less than 40 chars)\n")
    
    if need_validation in project_name:
       break
    else:
       print("Invalid input!, try again.")
       num_of_tries = num_of_tries + 1
        
    if num_of_tries == 3:
      exit()
            
    data_validation(project_name)
   
      
  author_name = input("Who is the Author of the project? (needs to be less than 40 chars)\n")
  if len(author_name) == 0:
     print("Invalid Input!, enter at least 1 char")
     exit()
  else:
    data_validation(author_name)
  
  print(" ")
  project_details = f" ## Project Details ## \n Project name: {project_name}\n Author:       {author_name}"
  time.sleep(1)
  print(project_details)
  
  # creation of the directory and mardowm files
  path = "E:/Python_Projects"
  project_name_path = f"{author_name}/{project_name}"
  joined_paths = os.path.join(path,project_name_path)

  try:
      os.makedirs(joined_paths)
      print(f"Created Directory at %s" % joined_paths)
  except FileExistsError:
      print("File already present in directory")
  
  readme_file = "README.md"
  readme_dir = os.path.join(joined_paths,readme_file)
  
  with open(readme_dir, "w") as file:
     file.write(f"## Welcome to {project_name}\n")
     file.write(" \n")
     file.write(f"## Description\n")
     file.write(" \n")
     file.write(f"## How to run/install project\n")
     file.write(" \n")
     file.write(f"Created by {author_name}") 
  print("README file created %s" %readme_dir)

  python_file = "main.py"
  python_dir = os.path.join(joined_paths, python_file)
  with open(python_dir, "w") as file:
     file.write('if __name__ == "__main__":')
  print("Python file created %s" %python_dir)


if __name__ == "__main__":
   main()