#List all the files
import os
print(os.listdir())
#Environment Variables

#Set the environment variable
os.environ['var'] = 'vyshnav'
print(os.getenv('var')) # Get environment variable