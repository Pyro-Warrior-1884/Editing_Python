from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os,sys

def edit_crop(region):
    save = region
    while True:
        print("Options")
        print("0: Save Cropped Image \n1: Sharpen \n2: Contrast \n3: Brightness \n4: Colour \n5: Convert Black & White \n6: Blur \n8: Rotate \n9: Transpose \n10: Changes History \n11: Reset Image \n")
        choice = int(input("Enter Your Choice: "))
        if choice == 0:            
            return region

        elif choice == 1:
            factor = float(input("Enter the Increase Factor: "))
            enhancer = ImageEnhance.Sharpness(region)
            region = enhancer.enhance(factor)
            Changes.append([len(Changes)+1,"Crop Sharpen","Factor: "+str(factor)])
            print("Change Applied\n")
                
        elif choice == 2:
            factor = float(input("Enter the Increase Factor: "))
            enhancer = ImageEnhance.Contrast(region)
            region = enhancer.enhance(factor)
            Changes.append([len(Changes)+1,"Crop Contrast","Factor: "+str(factor)])
            print("Change Applied\n")
    
        elif choice == 3:
            factor = float(input("Enter the Increase Factor: "))
            region = ImageEnhance.Brightness(region)
            region = region.enhance(factor)
            Changes.append([len(Changes)+1,"Crop Brightness","Factor: "+str(factor)])
            print("Change Applied\n")
    
        elif choice == 4:
            factor = float(input("Enter the Increase Factor: "))
            region = ImageEnhance.Color(region)
            region = region.enhance(factor)
            Changes.append([len(Changes)+1,"Crop Color","Factor: "+str(factor)])
            print("Change Applied\n")

        elif choice == 5:
            region = region.convert('L')
            Changes.append([len(Changes)+1,"Crop Black & White"," "])
            print("Change Applied\n")

        elif choice == 6:
            radius = int(input("Enter Positive Value: "))
            while radius < 0:
                radius = int(input("Enter Positive Value: "))
            region = region.filter(ImageFilter.GaussianBlur(radius))
            Changes.append([len(Changes)+1,"Crop Blur","Factor: "+str(radius)])
            print("Change Applied\n")

        elif choice == 9:
            degree = int(input("Enter Degrees to Rotate: "))
            region = region.rotate(degree)
            Changes.append([len(Changes)+1,"Crop Rotate","Degree: "+str(degree)])
            print("Change Applied\n")

        elif choice == 10:
            Direction = int(input("Enter Direction (1.Flip Left Right/2.Flip Top Bottom): "))
            while Direction not in [1,2]:
                Direction = int(input("Wrong Input Re-Enter: "))

            if Direction == 1:
                region = region.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
                Changes.append([len(Changes)+1,"Crop Transpose","Direction: Flip Left Right"])
            elif Direction == 2:
                region = region.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
                Changes.append([len(Changes)+1,"Crop Transpose","Direction: Flip Top Bottom"])                
            print("Change Applied\n")             

        elif choice == 11:
            print()
            for i in range(len(Changes)):
                print(Changes[i][0],' ',Changes[i][1],' ',Changes[i][2])    
            print()      

        elif choice == 12:
            region = save
            print("Cropped Image has been Reseted\n")

        else:
            print("Invalid Choice") 

path = input("Enter the Path where image is stored: ")
pathOut = input("Enter the Path to save edited image: ")

print("Hello")
while True:
    ch = input("Would You Like to Edit an Image(y/n): ")
    if ch.upper() == 'Y':
        filename = input("Enter the Filename: ")

        img = Image.open(os.path.join(path, filename))
        print("\nImage Format:",img.format)
        print("Image Size:",img.size)   
        print("Image Mode:",img.mode) 
        print()
        edit = img
        Changes = []

        while True:
            print("Options")
            print("0: Save Image as Copy \n1: Sharpen \n2: Contrast \n3: Brightness \n4: Colour \n5: Convert Black & White \n6: Blur \n7: Rotate \n8: Resize \n9: Transpose \n10: Crop \n11: Changes History \n12: Reset Image \n")
            
            choice = int(input("Enter Your Choice: "))

            if choice == 0:
                os.makedirs(pathOut, exist_ok=True)
                clean_name, ext = os.path.splitext(filename)
                edit.save(os.path.join(pathOut, f"{clean_name}_edited{ext}"))
                print(f"\nImage saved successfully at: {os.path.join(pathOut, f'{clean_name}_edited{ext}')} \n")
                ask = input("Do You Wish To Exit (y/n): ")
                if ask.upper() == 'Y':
                    Changes = []
                    break

            elif choice == 1:
                factor = float(input("Enter the Increase Factor: "))
                enhancer = ImageEnhance.Sharpness(edit)
                edit = enhancer.enhance(factor)
                Changes.append([len(Changes)+1,"Sharpen","Factor: "+str(factor)])
                print("Change Applied\n")
                
            elif choice == 2:
                factor = float(input("Enter the Increase Factor: "))
                enhancer = ImageEnhance.Contrast(edit)
                edit = enhancer.enhance(factor)
                Changes.append([len(Changes)+1,"Contrast","Factor: "+str(factor)])
                print("Change Applied\n")
    
            elif choice == 3:
                factor = float(input("Enter the Increase Factor: "))
                edit = ImageEnhance.Brightness(edit)
                edit = edit.enhance(factor)
                Changes.append([len(Changes)+1,"Brightness","Factor: "+str(factor)])
                print("Change Applied\n")
    
            elif choice == 4:
                factor = float(input("Enter the Increase Factor: "))
                edit = ImageEnhance.Color(edit)
                edit = edit.enhance(factor)
                Changes.append([len(Changes)+1,"Color","Factor: "+str(factor)])
                print("Change Applied\n")

            elif choice == 5:
                edit = edit.convert('L')
                Changes.append([len(Changes)+1,"Black & White"," "])
                print("Change Applied\n")

            elif choice == 6:
                radius = int(input("Enter Positive Value: "))
                while radius < 0:
                    radius = int(input("Enter Positive Value: "))
                edit = edit.filter(ImageFilter.GaussianBlur(radius))
                Changes.append([len(Changes)+1,"Blur","Factor: "+str(radius)])
                print("Change Applied\n")

            elif choice == 7:
                degree = int(input("Enter Degrees to Rotate: "))
                edit = edit.rotate(degree)
                Changes.append([len(Changes)+1,"Rotate","Degree: "+str(degree)])
                print("Change Applied\n")

            elif choice == 8:
                print(edit.size)
                x_axis = int(input("Enter New X Axis: "))
                y_axis = int(input("Enter New Y Axis: "))
                while x_axis < 0:
                    x_axis = int(input("Enter New Positive X Axis: "))
                while y_axis < 0:
                    y_axis = int(input("Enter New Positive Y Axis: "))
                
                edit = edit.resize((x_axis,y_axis))
                Changes.append([len(Changes)+1,"Resize","New Size: "+str((x_axis,y_axis))])
                print("Change Applied\n")

            elif choice == 9:
                Direction = int(input("Enter Direction (1.Flip Left Right/2.Flip Top Bottom): "))
                while Direction not in [1,2]:
                    Direction = int(input("Wrong Input Re-Enter: "))

                if Direction == 1:
                    edit = edit.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
                    Changes.append([len(Changes)+1,"Transpose","Direction: Flip Left Right"])
                elif Direction == 2:
                    edit = edit.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
                    Changes.append([len(Changes)+1,"Transpose","Direction: Flip Top Bottom"])                
                print("Change Applied\n")     

            elif choice == 10:
                print("Size of the Image: ",edit.size)
                size = list(edit.size)
                x = size[0]
                y = size[1]

                crop_way = int(input("Do You want to 1. Crop the image or 2. Edit a part of the image: "))
                while crop_way not in [1,2]:
                    crop_way = int(input("Enter 1 or 2: "))
                
                left_parameter = int(input("Enter the Left Parameter: "))
                while left_parameter < 0 or left_parameter > y:
                    print("Left parameter must be more than 0 and less than or equal to",y)                    
                    left_parameter = int(input("Enter Corrected Left Parameter: "))
                
                right_parameter = int(input("Enter the Right Parameter: "))
                while right_parameter < 0 or right_parameter > y:
                    print("Right parameter must be more than 0 and less than or equal to",y)                    
                    right_parameter = int(input("Enter Corrected Right Parameter: "))

                upper_parameter = int(input("Enter the Upper Parameter: ")) 
                while upper_parameter < 0 or upper_parameter > x:
                    print("Upper parameter must be more than 0 and less than or equal to",x)                    
                    upper_parameter = int(input("Enter Corrected Upper Parameter: "))

                lower_parameter = int(input("Enter the Lower Parameter: "))
                while lower_parameter < 0 or lower_parameter > y:
                    print("Lower parameter must be more than 0 and less than or equal to",x)                    
                    lower_parameter = int(input("Enter Corrected Lower Parameter: "))                

                while right_parameter < left_parameter:
                    print("Left parameter must be less than right parameter",right_parameter)
                    left_right = int(input("Do you want to change the 1. right or 2. left: " ))
                    if left_right == 1:
                        right_parameter = int(input("Enter Corrected Right Parameter: "))
                    else:
                        left_parameter = int(input("Enter Corrected Left Parameter: "))
                
                while upper_parameter > lower_parameter:
                    print("Upper parameter must be less than Lower parameter",right_parameter)
                    left_right = int(input("Do you want to change the 1. upper or 2. lower: " ))
                    if left_right == 1:
                        upper_parameter = int(input("Enter Corrected Upper Parameter: "))
                    else:
                        lower_parameter = int(input("Enter Corrected Lower Parameter: "))
                print()

                box = (left_parameter, upper_parameter, right_parameter, lower_parameter)

                if crop_way == 1:
                    region = edit.crop(box)
                    edit = region
                    Changes.append([len(Changes)+1,"Cropped","Parameters: "+str(box)])                  
                
                else:
                    region = edit.crop(box)
                    region = edit_crop(region)
                    edit.paste(region,box)
                    Changes.append([len(Changes)+1,"Cropped Edited","Parameters: "+str(box)])
                print("Change Applied\n")           


            elif choice == 11:
                print()
                if len(Changes) == 0:
                    print("No Changes Made")
                else:
                    for i in range(len(Changes)):
                        print(Changes[i][0],' ',Changes[i][1],' ',Changes[i][2])    
                    print()      

            elif choice == 12:
                edit = img
                print("Edit has been Reseted\n")

            else:
                print("Invalid Choice")                     
        
    elif ch.upper() == 'N':
        print("Thank You & Goodbye\n")
        break

    else:
        print("Invalid Input")

