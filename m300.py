import getopt
import sys

from p210_hoo_goa_chu_im_all import main_run as hoo_goa_chu_im_all


def myfunc(argv):
    arg_input = ""
    arg_output = ""
    arg_user = ""
    # arg_help = "{0} -i <input> -u <user> -o <output>".format(argv[0])
    arg_help = f"{argv[0]} -i <input> -u <user> -o <output>"

    try:
        opts, args = getopt.getopt(argv[1:], "hi:u:o:", ["help", "input=",
                                                         "user=", "output="])
    except:
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

    return {
        'input': arg_input,
        'user': arg_user,
        'output': arg_output,
    }


if __name__ == "__main__":
    # 取得 Input 檔案名稱
    opts = myfunc(sys.argv)
    if opts['input'] != "":
        CONVERT_FILE_NAME = opts['input']
    else:
        CONVERT_FILE_NAME = 'hoo-goa-chu-im.xlsx'
    print(f"CONVERT_FILE_NAME = {CONVERT_FILE_NAME}")

    # 將已填入注音之「漢字注音表」，製作成 HTML 格式的各式「注音／拼音／標音」。
    hoo_goa_chu_im_all(CONVERT_FILE_NAME)
