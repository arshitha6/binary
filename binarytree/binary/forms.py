from django import forms
from .models import BinaryTree

class BinaryTreeNodeForm(forms.ModelForm):
    class Meta:
        model = BinaryTree
        fields = ['name', 'node_id', 'parent']
        widgets = {
            'parent': forms.RadioSelect(choices=((None, 'None'),)),
        }

    left_or_right = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')], widget=forms.RadioSelect)

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        if self.instance.pk:
            self.fields['parent'].widget.choices = [(self.instance.pk, str(self.instance))]
            self.fields['left_or_right'].label = 'Add as left or right child of:'
        else:
            self.fields['left_or_right'].label = 'Add as root node'

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data['left_or_right'] == 'left':
            instance.parent = self.cleaned_data['parent'].left_child if self.cleaned_data['parent'] else None
        else:
            instance.parent = self.cleaned_data['parent'].right_child if self.cleaned_data['parent'] else None
        if commit:
            instance.save()
        return instance