import os, sys, csv, json

def extract_info(path, csv_writer, json_data):
    contains = False
    for filename in ["requirements.txt", "package.json"]:
        file_path = os.path.join(path, filename)
        if os.path.exists(file_path):
            contains = True
            with open(file_path, "r") as f:
                if filename.endswith(".txt"):
                    name, version = f.read().split("==")
                    t = "pip"
                else:
                    data = json.load(f)
                    name = data["name"]
                    version = data["version"]
                    t = "npm"
                csv_writer.writerow([name, version, t, file_path])
                json_data.append({"name": name, "version": version, "type": t, "path": file_path})
    
    #Sends a message to user in case they have forgoten to add the must have files to the direcotry
    if contains is False:
        print(f'{path} doesn´t include a requirements.txt or a package.json file')

def main(path):
    resository_count = 0
    json_data = []
    with open(os.path.join(path, "sbom.csv"), "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Name", "Version", "type", "path"])
        
        for dir_name in os.listdir(path):
            new_dir_path = os.path.join(path, dir_name)
            if os.path.isdir(new_dir_path):
                resository_count += 1
                extract_info(new_dir_path, csv_writer, json_data)

    with open(os.path.join(path, "sbom.json"), "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Found {resository_count} repositories in ´{path}´")
    print(f"Saved SBOM in CSV format to ´{os.path.join(path, 'sbom.csv')}´")
    print(f"Saved SBOM in json format to ´{os.path.join(path, 'sbom.json')}´")

if __name__ == "__main__":
    main(sys.argv[1])