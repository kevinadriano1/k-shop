from django.shortcuts import render

def show_main(request):
    context = {
        'products': [
            {
                'name': 'barcelona 2024',
                'price': 100,
                'description': 'this is great product with excellent features!',
                'image_url': 'https://down-id.img.susercontent.com/file/id-11134207-7r98z-lsh0i1i3mid960'  # Add the image URL here
            },
            {
                'name': 'manchester united 2024',
                'price': 200,
                'description': 'this product is the best in the market!',
                'image_url': 'https://footdealer.co/wp-content/uploads/2024/08/Maillot-de-face-Manchester-United-Domicile-2024-2025.jpg'  # Add the image URL here
            },
            {
                'name': 'real madrid 2024',
                'price': 150,
                'description': 'great product excellent features!',
                'image_url': 'https://footdealer.co/wp-content/uploads/2023/06/Mailllot-Match-Real-Madrid-Domicile-2023-2024-1.jpg'  # Add the image URL here
            }
        ],
    }
    return render(request, 'main.html', context)
