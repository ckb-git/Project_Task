from django import forms  
from imsapp.models import Inventory , Orders, Transaction
class inventoryForm(forms.ModelForm):  
    class Meta:  
        model = Inventory  
        # fields='__all__'
        fields = ['name','cost','selling_price','quantity'] 
        widgets = { 
            'name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'quantity':forms.TextInput(attrs={ 'class': 'form-control' }),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
            'selling_price': forms.TextInput(attrs={'class': 'form-control'}),  
                    #forms.DecimalField(max_length = 200)
      }
    def clean_selling_price(self):
        valcost=self.cleaned_data['cost']
        valsp=self.cleaned_data['selling_price']
        
        if (valsp<2*valcost):
            raise forms.ValidationError("wrong  amount")
        elif (valcost<=0):
            raise forms.ValidationError("enter currect cost")
        return valsp
    
    def clean_name(self):
        val_name=self.cleaned_data['name']
        if (len(val_name)<3):
            raise forms.ValidationError("enter currect Name")
        return val_name
    
class ordersForm(forms.ModelForm): 
    name=forms.CharField(required=True,widget=forms.TextInput(attrs={'readonly':'readonly'})) 
    quantity=forms.IntegerField(required=True,min_value=1)
    selling_price= forms.DecimalField(required=True)

    class Meta:  
        model = Orders  
        fields=['name','item','quantity','selling_price']

    # def clean_quantity(self):
    #     val_quantity=self.cleaned_data['quantity']
    #     if (val_quantity<3):
    #         raise forms.ValidationError("enter currect Name")
    #     return val_quantity


class transactionForm(forms.ModelForm): 
    name=forms.CharField(required=True) 
    quantity=forms.IntegerField(required=True)
    selling_price= forms.IntegerField(required=True)
    status=forms.CharField(required=True) 
    
    class Meta:  
        model = Transaction  
        fields=['name','orid','quantity','selling_price','status']
   

    
       
         
    
        