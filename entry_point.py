from scoring.StudyService import StudyService
import getopt
import sys


def main(argv):
    config_path = ''
    input_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:c:", ["ifile=", "cfile="])
    except getopt.GetoptError as ge:
        print("run -i <inputfile> -c <configfile>")
        print("Getopt error({0})".format(ge))
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("-i <inputfile> -c <configfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-c", "--cfile"):
            config_path = arg

    StudyService.run_study(input_file, config_path)

if __name__ == "__main__":
    main(sys.argv[1:])
