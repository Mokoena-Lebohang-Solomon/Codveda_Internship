import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users():
    try:
        response = requests.get(
            API_URL,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            print("Unexpected API response.")
            return []

        return data

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except ValueError:
        print("Error: The API returned invalid JSON.")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")

    return []


def display_users(users):
    if not users:
        print("No users found.")
        return

    print("\n" + "=" * 70)
    print("USERS FROM API")
    print("=" * 70)

    for user in users:
        print(f"ID:       {user['id']}")
        print(f"Name:     {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Email:    {user['email']}")
        print(f"Company:  {user['company']['name']}")
        print("-" * 70)


def main():
    print("Fetching users from API...")

    users = fetch_users()

    display_users(users)


if __name__ == "__main__":
    main()