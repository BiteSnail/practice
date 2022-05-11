import sys
import pdb

def test_logger():
    """Test logger.
    :return: test result.
    :rtype: bool
    """
    from practice.src import mylogger

    try:
        m = mylogger.get_logger('test', '/home/upright/practice/log')
        m.debug('hi, debug')
    except Exception as e:
        print(e)
        return False
    return True

def test_config():
    """Test config.

    :return: test result.
    :rtype: bool
    """
    
    from practice.src import myconfig
    try:
        m = myconfig.get_config('/home/upright/practice/share/test.config')
        print('key=1', m['general'].get('key1'))
        print('key=2', m['general'].get('key2'))
        print('key=3', m['logger'].get('key3'))
    except Exception as e:
        print(e)
        return False
    return True

if __name__ == '__main__':
    target_step = []
    if len(sys.argv) >= 2:
        target_step = sys.argv[1].split(',')
    print('Test steps = ', target_step)

    if not target_step or 'logger' in target_step:
        ret = test_logger()
        if not ret:
            raise Exception('Error when test_logger')
        print('Success - test_logger')

    if not target_step or 'config' in target_step:
        ret = test_config()
        if not ret:
            raise Exception('Error when test_config')
        print('Success - test_config')
    print('Test completed.')
