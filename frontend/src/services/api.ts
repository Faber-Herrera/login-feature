import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
});

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export const authApi = {
  login: async (email: string, password: string): Promise<LoginResponse> => {
    const params = new URLSearchParams();
    params.append('username', email);
    params.append('password', password);
    
    const { data } = await api.post<LoginResponse>('/auth/login', params);
    return data;
  }
};