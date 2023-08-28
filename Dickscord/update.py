from .imports import *

def __lastversion__(package_name):
    response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    data = response.json()
    return data["info"]["version"]

def __update__(package_name):
    try:
        current_version = pkg_resources.get_distribution(package_name).version
        latest_version = __lastversion__(package_name)        
        if current_version != latest_version:
            subprocess.check_call(['pip', 'install', '--upgrade', package_name])
            Style.print(f"(+): {package_name} is now updated.")
        else:
            pass
    except Exception as e:
        Style.print(f"(!): Error when updating Dickscord: {e}")

__update__("Dickscord")