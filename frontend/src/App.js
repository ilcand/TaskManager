import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';


const API_URL = "http://localhost:8000/tasks";

function App() {
  const [tasks, setTasks] = useState([]);
  const [form, setForm] = useState({ title: "", description: "" });

  useEffect(() => {
    axios.get(API_URL).then(res => setTasks(res.data));
  }, []);

  const createTask = async () => {
    if (!form.title) return alert("Title is required!");
    await axios.post(API_URL, form);
    const res = await axios.get(API_URL);
    setTasks(res.data);
    setForm({ title: "", description: "" });
  };

  const toggleStatus = async (id) => {
    await axios.put(`${API_URL}/${id}`);
    const res = await axios.get(API_URL);
    setTasks(res.data);
  };

  const deleteTask = async (id) => {
    await axios.delete(`${API_URL}/${id}`);
    const res = await axios.get(API_URL);
    setTasks(res.data);
  };

  return (
    <div className="App">
      <h1>Task Manager</h1>
      <input placeholder="Title" value={form.title} onChange={e => setForm({...form, title: e.target.value})} />
      <input placeholder="Description" value={form.description} onChange={e => setForm({...form, description: e.target.value})} />
      <button onClick={createTask}>Add Task</button>
      <ul>
        <li style={{ display: "flex", justifyContent: "left", alignContent: "center", gap: "9.25rem"}}>
          <strong style={{ display: "inline-block", width: "1rem" }}>Title</strong>
          <strong style={{ }}>Description</strong>
        </li>
        {tasks.map(task => (
          <li key={task.id}  style={{
            backgroundColor: task.status ? '#7FD848' : 'strong',
            padding: '0.5rem',
            marginBottom: '0.5rem',
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            borderRadius: '4px'
            }}>
            <span style={{ textDecoration: task.status ? 'line-through' : 'none', display: "inline-block", width: "150px" }}>
              {task.title}
            </span>
            {task.description && (
              <span style={{ textDecoration: task.status ? 'line-through' : 'none' }}>
                {task.description}
              </span>
            )}
            <button onClick={() => toggleStatus(task.id)}>Toggle</button>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;