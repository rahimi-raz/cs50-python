file_name=input("Please enter your file name: ").strip().lower()
number_of_dots=file_name.count('.')

if number_of_dots == 0:
    print("application/octet-stream")
else:
    extention=file_name.split('.')[-1]
    match extention:
        case "jpg":
            print("image/jpeg")

        case "jpeg":
            print("image/jpeg")

        case "pdf":
            print("application/pdf")

        case "gif":
            print("image/gif")

        case "png":
            print("image/png")

        case "txt":
            print("text/plain")

        case "zip":
            print("application/zip")

        case default:
            print("application/octet-stream")