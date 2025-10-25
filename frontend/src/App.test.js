import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('AI Fighter App', () => {
  test('renders login form', () => {
    render(<App />);
    
    // Check for main elements
    expect(screen.getByText('AI Fighter App')).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: 'Login' })).toBeInTheDocument();
    expect(screen.getByLabelText(/username/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /login/i })).toBeInTheDocument();
  });

  test('handles input changes', () => {
    render(<App />);
    
    const usernameInput = screen.getByLabelText(/username/i);
    const passwordInput = screen.getByLabelText(/password/i);
    
    fireEvent.change(usernameInput, { target: { value: 'testuser' } });
    fireEvent.change(passwordInput, { target: { value: 'password123' } });
    
    expect(usernameInput.value).toBe('testuser');
    expect(passwordInput.value).toBe('password123');
  });

  test('displays error message on failed login', async () => {
    render(<App />);
    
    // Mock failed fetch
    global.fetch = jest.fn(() =>
      Promise.reject(new Error('Failed to connect'))
    );
    
    const loginButton = screen.getByRole('button', { name: /login/i });
    fireEvent.click(loginButton);
    
    // Wait for error message
    const errorMessage = await screen.findByText('An error occurred. Please try again later.');
    expect(errorMessage).toBeInTheDocument();
  });
});
