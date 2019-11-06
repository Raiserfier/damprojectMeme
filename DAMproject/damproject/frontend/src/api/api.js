import axios from 'axios'

let local_host = 'http://127.0.0.1:8000';

export const register = parmas => { return axios.post(`${local_host}/register/`, parmas) }
