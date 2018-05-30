import commands, program

class TestProcessArgs():
    def test_basic(self):
        args = program.process_args("arg1 arg2 arg3")
        assert args[0] == "arg1"
        assert args[1] == "arg2"
        assert args[2] == "arg3"

    def test_extra_spaces(self):
        args = program.process_args("arg1  arg2   arg3")
        assert args[0] == "arg1"
        assert args[1] == "arg2"
        assert args[2] == "arg3"

    def test_with_quotes(self):
        args = program.process_args("arg1 \"arg2 still arg2\"")
        assert args[0] == "arg1"
        assert args[1] == "arg2 still arg2"

    def test_1_extra_quote(self):
        args = program.process_args("arg1 \" arg2 arg3")
        assert args[0] == "arg1"
        assert args[1] == "\""
        assert args[2] == "arg2"
        assert args[3] == "arg3"

    def test_2_extra_quotes(self):
        args = program.process_args("arg1 \"\" arg2 arg3")
        assert args[0] == "arg1"
        assert args[1] == "arg2"
        assert args[2] == "arg3"

    def test_3_extra_quotes(self):
        args = program.process_args("arg1 \"\"\" arg2 arg3")
        assert args[0] == "arg1"
        assert args[1] == "\""
        assert args[2] == "arg2"
        assert args[3] == "arg3"

    def test_escaped_quote(self):
        args = program.process_args("arg1 arg2 arg\\\"3 arg4")
        assert args[0] == "arg1"
        assert args[1] == "arg2"
        assert args[2] == "arg\"3"
        assert args[3] == "arg4"

    def test_escaped_quote_in_quotes(self):
        args = program.process_args("arg1 \"arg2 arg\\\"3 arg4\"")
        assert args[0] == "arg1"
        assert args[1] == "arg2 arg\"3 arg4"
