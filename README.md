# Shopping Cart Project

This is an example Python application for users/customers to input one or more product identifiers and have their itemized receipt with the total amount owed. 

## Prerequisite 

+ Anaconda 3.7 +
+ Python 3.7 +
+ Pip 

## Installation 
Fork this [remote repository](https://github.com/susanna00/shopping-cart) under your own control, and "clone" or download your copy of the repository onto your local computer. 

Then navigate there from your command-line application: 

```sh 
cd shopping-cart
```

As previously pointed out in the prerequisite, you need to create and activate a new virtual environment, called "shopping-env":

```
conda create -n shopping-env python=3.8
conda activate shopping-env
```
From inside the virtual environment, install package dependencies:

```
pip install -r requirements.txt
```
>NOTE: Make sure you are running it from the repository's root directory, to ensure the command does not display an error message. 

## Setup 

In the root directory of your local repository, create a new file called ".env", and update the content of the ".env" file to specify the tax rate that must be applied depending on your location, see example below:

    TAX_RATE= 0.0875

## Usage 

Run the shopping cart script from the command-line:

    python shopping_cart.py 

Different items will be displayed, type items' IDs, and type DONE when you are done with your shopping list. 

The products chosen with the respective prices in USD dollars will be displayed, along with the Subtotal, Taxes applied to your purchase, the Total, and a farewell message. 

