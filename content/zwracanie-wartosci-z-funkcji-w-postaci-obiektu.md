Title: Zwracanie wartości z funkcji w postaci obiektu
Date: 2011-11-14 22:05
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: ErrorReporting, raportowanie błędów, return
Slug: zwracanie-wartosci-z-funkcji-w-postaci-obiektu
Status: published

    PHP

    [code language="php"]

    class ErrorReporting {

        const INFO = 0;

        const WARNING = 1;

        const ERROR = 2;

        const SUCCESS = 4;
    private $_message = '';

        private $_class = '';

        private $_type;

        private $_value = null;
    /**

         *

         * @param ErrorReportingType $type

         * @param mixed $value

         * @param String $message

         */

        public function __construct($type, $value, $message = '') {

            $this->_type = $type;

            $this->_value = $value;

            $this->_message = $message;

            switch($this->_type) {

                case ErrorReporting::ERROR:

                    $this->_class = 'error';

                    break;

                case ErrorReporting::WARNING:

                    $this->_class = 'warning';

                    break;

                case ErrorReporting::INFO:

                    $this->_class = 'info';

                    break;

                case ErrorReporting::SUCCESS:

                    $this->_class = 'success';

                    break;

            }

        }
    /**

         *

         * @param String $key

         * @return mixed

         */

        public function __get($key) {

            switch($key) {

                case 'Message':

                    return $this->_message;

                    break;

                case 'Class':

                    return $this->_class;

                    break;

                case 'Type':

                    return $this->_type;

                    break;

                case 'Value':

                    return $this->_value;

                    break;

            }

        }
    /**

         *

         * @param String $key

         * @param mixed $value

         * @return mixed

         */

        public function __set($key, $value) {

            switch($key) {

                case 'Message':

                    return $this->_message = $value;

                    break;

                case 'Class':

                    return $this->_class = $value;

                    break;

                case 'Type':

                    return $this->_type = $value;

                    break;

                case 'Value':

                    return $this->_value = $value;

                    break;

            }

        }
    public function __toString() {

            return '<div class="'.$this->_class.'">'.$this->_message.'</div>';

        }

    }

    [/code]
    CSS
    [code language="css"]

    .success {background-image: url(../images/accept.png); background-color: #dff2bf; color:#4f8a10}

    .error, .error_message {background-image: url(../images/exclamation.png); background-color: #ffbaba; color:#d8000c}

    .info {background-image: url(../images/information.png); background-color:#bde5f8; color:#00529b}

    .warning {background-image: url(../images/error.png); background-color:#feefb3; color:#9f6000}

    .info,

    .success,

    .warning,

    .error,

    .validation,

    .error_message {border: 1px solid; margin: 10px auto; padding: 4px 10px 4px 35px; background-repeat: no-repeat; background-position: 10px 6px}

    .success ul,

    .error ul,

    .warning ul,

    .info ul {list-style: disc}

    .success li,

    .error li,

    .warning li,

    .info li {margin-left: 20px}

    [/code]
    Ikonki, których użycie warto rozważyć to np.: famfamfam.com lub Knob icon set.

    Cała paczka gotowa do pobrania: ErrorReporting
