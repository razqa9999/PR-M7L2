# user_management.py

def initialize_users():
    """Mengembalikan kamus pengguna yang telah ditentukan sebelumnya."""
    return {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3",
        "user4": "password4",
        "user5": "password5",
    }

def add_user(users, username, password):
    """Menambahkan pengguna baru jika belum ada dalam kamus.
    Mengembalikan kamus pengguna yang diperbarui."""
    # Tugas: jika pengguna sudah ada, kembalikan pesan - "Pengguna dengan username ini sudah terdaftar."
    if username in users:
        return "Pengguna dengan username ini sudah terdaftar."
    # Tugas: jika pengguna belum ada dalam kamus, tambahkan entri baru ke kamus dengan kunci sebagai username dan nilai sebagai password.
    users[username] = password
    return f"Pengguna baru {username} berhasil ditambahkan."

def display_users(users):
    """Menampilkan daftar semua pengguna dan password mereka."""
    print("Pengguna berikut sudah terdaftar dengan password mereka:")
    for username, password in users.items():
        print(f"Username: {username}, Password: {password}")

def main():
    users = initialize_users()
    display_users(users)

    print("\nAnda dapat menambahkan pengguna baru.")
    username = input("Masukkan username pengguna baru: ")
    password = input("Masukkan password pengguna baru: ")
    result = add_user(users, username, password)
    print(result)

    print("\nDaftar semua pengguna setelah penambahan:")
    display_users(users)

if __name__ == "__main__":
    main()
