import getopt
import sys


def myfunc(argv):
    arg_input = ""
    arg_output = ""
    arg_user = ""
    # arg_help = "{0} -i <input> -u <user> -o <output>".format(argv[0])
    arg_help = f"{argv[0]} -i <input> -u <user> -o <output>"

    try:
        opts, args = getopt.getopt(argv[1:], "hi:u:o:", ["help", "input=",
                                                         "user=", "output="])
    except Exception as err_msg:
        # handle any other exception
        print("Error '{0}' occured. Arguments {1}.".format(err_msg.message, err_msg.args))
        # Excecutes if no exception occured
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-i", "--input"):
            arg_input = arg
        elif opt in ("-u", "--user"):
            arg_user = arg
        elif opt in ("-o", "--output"):
            arg_output = arg

    print('input:', arg_input)
    print('user:', arg_user)
    print('output:', arg_output)


if __name__ == "__main__":
    myfunc(sys.argv)
