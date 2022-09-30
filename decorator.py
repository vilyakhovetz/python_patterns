# Decorator is a structural design pattern that allows you to dynamically add new functionality to objects by
# wrapping them in useful wrappers.

# Common Component interface.
class DataSource:
    def read_data(self):
        raise NotImplementedError("Method is not implemented!")

    def write_data(self, data):
        raise NotImplementedError("Method is not implemented!")


# One of the specific Components that implements the basic functionality.
class FileDataSource(DataSource):
    def __init__(self, filename):
        self.file = filename

    def read_data(self):
        print('Data read from file')

    def write_data(self, data):
        print('Data written to file')


# The parent of all Decorators contains the wrapping code.
class DataSourceDecorator(DataSource):
    def __init__(self, source):
        self.wrapper = source

    def read_data(self):
        return self.wrapper.read_data()

    def write_data(self, data):
        self.wrapper.write_data(data)


# Concrete Decorators add something of their own to the basic behavior of the wrapped Component.
class EncryptionDecorator(DataSourceDecorator):
    def read_data(self):
        print('Data received from the read_data method of the wrapped object (wrapper).')
        self.wrapper.read_data()
        print('The data is decrypted.')

    def write_data(self, data):
        print('Data is encrypted.')
        self.wrapper.write_data(data)


# You can decorate not only base Components, but already wrapped objects.
class CompressionDecorator(DataSourceDecorator):
    def read_data(self):
        print('Data received from the read_data method of the wrapped object (wrapper).')
        self.wrapper.read_data()
        print('The data is decompressed.')

    def write_data(self, data):
        print('Data is compressed.')
        self.wrapper.write_data(data)


if __name__ == '__main__':
    # 1. A simple example of building and using decorators.
    source = FileDataSource('file.dat')
    source.write_data('data')
    # Clean data has been written to the file.
    print()
    source = CompressionDecorator(source)
    source.write_data('data')
    # Compressed data has been written to the file.
    print()
    source = EncryptionDecorator(source)
    # source is a bunch of three objects: Encryption > Compression > FileDataSource
    source.write_data('data')
    # Compressed and encrypted data was written to the file.
