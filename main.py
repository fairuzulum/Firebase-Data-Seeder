from firestore_service import add_data_in_batch

def main():
    data = [
        {'icon': 'https://cdn-icons-png.flaticon.com/128/3659/3659875.png', 'name': 'Clothing'},
        {'icon': 'https://cdn-icons-png.flaticon.com/128/3659/3659880.png', 'name': 'Furniture'},
        {'icon': 'https://cdn-icons-png.flaticon.com/128/3659/3659890.png', 'name': 'Books'},
        {'icon': 'https://cdn-icons-png.flaticon.com/128/3659/3659901.png', 'name': 'Toys'},
        {'icon': 'https://cdn-icons-png.flaticon.com/128/3659/3659907.png', 'name': 'Sports'},
        {'icon': 'https://cdn-icons-png.flaticon.com/128/3659/3659915.png', 'name': 'Beauty'},
        {'icon': 'https://cdn-icons-png.flaticon.com/128/3659/3659924.png', 'name': 'Food'},
        {'icon': 'https://cdn-icons-png.flaticon.com/128/3659/3659930.png', 'name': 'Automotive'},
        {'icon': 'https://cdn-icons-png.flaticon.com/128/3659/3659944.png', 'name': 'Garden'},
    ]
    add_data_in_batch(data)

if __name__ == '__main__':
    main()
