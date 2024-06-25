from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Input from Party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the sum and product
    sum_result = my_int1 + my_int2
    product_result = my_int1 * my_int2

    # Output the results to Party2
    sum_output = Output(sum_result, "sum_output", party2)
    product_output = Output(product_result, "product_output", party2)

    return [sum_output, product_output]

