from django.shortcuts import render, redirect
from .models import BinaryTree
from .forms import BinaryTreeNodeForm

def binary_tree_view(request):
    root_node = BinaryTree.objects.filter(parent=None).first()
    form = BinaryTreeNodeForm(request.POST or None, instance=BinaryTree())
    if form.is_valid():
        form.save()
        form = BinaryTreeNodeForm(instance=BinaryTree())
    search_node_id = request.GET.get('search')
    search_node = BinaryTree.objects.filter(node_id=search_node_id).first() if search_node_id else None
    return render(request, 'binary_tree.html', {
        'root_node': root_node,
        'form': form,
        'search_node': search_node,
    })