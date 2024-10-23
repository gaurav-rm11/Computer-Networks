

def decimal_to_binary(decimal, bits=8):
    return bin(decimal)[2:].zfill(bits)


def wrap_up_to_4_bits(value):
    while value > 0xF:
        value = (value & 0xF) + (value >> 4)
    return value


def calculate_checksum(data):
    total_sum = sum(data)
    print(f"Sum of the decimal numbers: {total_sum}")
    wrapped_sum = wrap_up_to_4_bits(total_sum)
    print(f"Wrapped up 4-bit sum: {decimal_to_binary(wrapped_sum, bits=4)}")
    checksum = (~wrapped_sum) & 0xF
    print(f"Complemented checksum (4 bits): {decimal_to_binary(checksum, bits=4)}")

    return checksum


def verify_checksum(data_with_checksum):
   
    total_sum = sum(data_with_checksum)
    print(f"\nReceiver's total sum: {total_sum}")
    
    wrapped_sum = wrap_up_to_4_bits(total_sum)
    print(f"Receiver's wrapped up 4-bit sum: {decimal_to_binary(wrapped_sum, bits=4)}")

    final_complement = (~wrapped_sum) & 0xF
    print(f"Final complement at receiver's end (4 bits): {decimal_to_binary(final_complement, bits=4)}")
    return final_complement == 0

def main():
    data = [8, 7, 8, 8, 0, 2, 2, 1, 8, 0]
    print("Original Data (Decimal):", data)

    checksum = calculate_checksum(data)

    transmitted_data = data + [checksum]
    print("\nTransmitted Data (Decimal):", transmitted_data)

    is_valid = verify_checksum(transmitted_data)
    print(f"\nIs the received data valid? {'Yes' if is_valid else 'No'}")

if __name__ == "__main__":
    main()
