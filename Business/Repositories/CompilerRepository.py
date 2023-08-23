import os,re
from subprocess import Popen, PIPE


class CompilerRepository:
    _compiler_aux_files_dir = os.path.join(os.path.dirname(__file__), 'CompilerAuxFiles')
    _filename = os.path.join(_compiler_aux_files_dir, 'script.py')
    _snippet_file =  os.path.join(_compiler_aux_files_dir,"snippet_for_function.py")



    def _write_in_file(self, source_code):
        with open(self._filename, "w") as write_file:
            write_file.write(source_code)

    def _append_in_file(self,source_code):
        with open(self._filename,"a") as append_file:
            append_file.write("\n")
            append_file.write(source_code)

    def _run_in_docker(self):
        # building the docker container according to the Dockerfile
        os.system("docker build -t python-machine {}".format(self._compiler_aux_files_dir))

        # os.system("docker container commit --change=\"CMD [\"python\",\"-u\",\"./script.py\"]\" 41da0144ca93 python_machine/test:1")

        # run the script.py in the docker container and provide the result
        proc = Popen('docker run python-machine', shell=True, stdout=PIPE, stderr=PIPE)

        # the result is a tuple (a,b) with:
        # a -> the stdout message
        # b -> the stderr message
        result_from_execution = proc.communicate()

        return result_from_execution

    def evaluate_simple_code_submission(self, source_code):
        self._write_in_file(source_code)
        return self._run_in_docker()

    def generalize_function(self,content,general_name):
        x = re.search("def .+\(", content).group()
        content = content.replace(x, "def {}(".format(general_name))
        return content

    def evaluate_function_submitted_by_user(self, source_code, resolved_code):

        source_code = self.generalize_function(source_code,"func_submitted")
        resolved_code = self.generalize_function(resolved_code,"func_resolved")
        snippet_for_test_cases = open(self._snippet_file,"r").read()
        self._write_in_file(source_code)
        self._append_in_file(resolved_code)
        self._append_in_file(snippet_for_test_cases)

        return self._run_in_docker()


