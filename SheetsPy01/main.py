# Create Needed classes for later
class List:
    def __init__(self, list_, name):
        self.content = list_
        self.name = name


class Cell:
    def __init__(self, y, x, content):
        self.y = y
        self.x = x
        self.content = content

    def change(self, new_content):
        self.content = new_content


# Create custom errors.
class Error(Exception):
    pass


class SpreadsheetError(Error):
    pass


# create the spreadsheet class
class Spreadsheet:
    def __init__(self, x_len, y_len):
        self.x_axis_list = []
        self.y_axis_list = []
        self.y_len = y_len
        self.x_len = x_len
        self._tuple = None
        self.output = []
        for y in range(y_len):
            alist = []
            for x in range(x_len):
                alist.append(Cell('X%s' % x, 'Y%s' % y, None))
            self.y_axis_list.append(List(alist, 'Y%s' % y))

        for x in range(x_len):
            alist = []
            for content in self.y_axis_list:
                alist.append(content.content[x])
            self.x_axis_list.append(List(alist, 'X%s' % x))

    def get_cell(self, x, y):
        try:
            if self.x_axis_list[y].content[x] == self.y_axis_list[x].content[y]:
                cell = self.y_axis_list[x].content[y]
                return cell.x, cell.y, cell.content
        except IndexError:
            raise SpreadsheetError('Requested index is outside of spreadsheet boundaries.')

    def change_cell(self, x, y, new_content):
        try:
            if self.x_axis_list[y].content[x] == self.y_axis_list[x].content[y]:
                cell = self.y_axis_list[x].content[y]
                cell.change(new_content)
        except IndexError:
            raise SpreadsheetError('Requested index is outside of spreadsheet boundaries.')

    def _get_format_num(self):
        floatnum = 0

        for a in self._tuple:
            x_axis = '|%s' * self.x_len
            x_axis = x_axis % a
            floatnum += len(x_axis)

        return round(floatnum / len(self._tuple))

    def format_selftuple(self, spaces=2):
        self._tuple = self._tuple = tuple(
            tuple(self.y_axis_list[num].content[i].content for i in range(len(self.y_axis_list[num].content))) for num
            in range(self.y_len))
        formated_tuple = []
        for a in self._tuple:
            for b in a:
                if len(str(b)) > spaces:
                    spaces = len(str(b))

        for a in self._tuple:
            alist = []
            for b in a:
                alist.append(' ' * (spaces - len(str(b))) + str(b))
            formated_tuple.append(tuple(alist))

        formated_tuple = tuple(formated_tuple)
        self._tuple = formated_tuple
        return self._tuple

    def _reset_selftuple(self):
        self._tuple = None

    def reset_output(self):
        self.output = []

    def pretty_print(self):
        for i in self.output:
            print(i)

    def pretty_output(self, formating=2):
        self.format_selftuple(spaces=formating)
        self._output_grid(num=self._get_format_num(), sub_tuples=self._tuple)
        self._reset_selftuple()

    def output_grid(self, sub_tuple=None):
        self._output_grid(sub_tuple=sub_tuple)

    def _output_grid(self, num=None, sub_tuple=None, sub_tuples=None):
        for i in range(self.y_len):
            x_axis = '|%s' * self.x_len
            if sub_tuple is None and sub_tuples is None:
                self.output.append(x_axis)
            elif sub_tuple is None:
                try:
                    self.output.append(x_axis % sub_tuples[i])
                except TypeError:
                    raise SpreadsheetError('Invalid tuple length for sub_tuple.')
            else:
                try:
                    self.output.append(x_axis % sub_tuple)
                except TypeError:
                    raise SpreadsheetError('Invalid tuple length for sub_tuple.')
            if num is None:
                num = 3
            self.output.append('-' * num)

