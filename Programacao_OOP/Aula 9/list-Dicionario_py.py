def main():
    l = [12,2,3,4,5,1,6,7,17,8,9,10,11,13,14,15,16,18,19,20]
    s = set(l)
    print(s)
    s.add(44)
    s.remove(1)
    print(s)
    
    a = {1,2,3}
    b = {3,4,5}
    
    print(a | b)
    print(a & b)
    print(a - b)
    
if __name__ == "__main__":
    main()