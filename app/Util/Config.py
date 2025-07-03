import cloudinary
import os

#SECRET_KEY="856b54f4547494f9247db2fdd5a633d2358966c9724e55bfce5a99fcec7af4bc"
#Algorithm="HS256"
SECRET_KEY=os.getenv("SECRET_KEY")
Algorithm=os.getenv("Algorithm")

cloudinary.config(
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    cloud_secret=os.getenv("CLOUDINARY_API_SECRET")
)