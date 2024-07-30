import React, { useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
    const [playerId, setPlayerId] = useState('');
    const [season, setSeason] = useState('');
    const [recentAvgPoints, setRecentAvgPoints] = useState('');
    const [homeAway, setHomeAway] = useState('');
    const [opponentAvgPointsAllowed, setOpponentAvgPointsAllowed] = useState('');
    const [predictedPoints, setPredictedPoints] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await axios.post('http://localhost:5000/predict', {
            player_id: playerId,
            season: season,
            recent_avg_points: recentAvgPoints,
            home_away: homeAway,
            opponent_avg_points_allowed: opponentAvgPointsAllowed
        });
        setPredictedPoints(response.data.predicted_points);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" value={playerId} onChange={(e) => setPlayerId(e.target.value)} placeholder="Player ID" required />
                <input type="text" value={season} onChange={(e) => setSeason(e.target.value)} placeholder="Season" required />
                <input type="number" value={recentAvgPoints} onChange={(e) => setRecentAvgPoints(e.target.value)} placeholder="Recent Avg Points" required />
                <input type="number" value={homeAway} onChange={(e) => setHomeAway(e.target.value)} placeholder="Home/Away (1/0)" required />
                <input type="number" value={opponentAvgPointsAllowed} onChange={(e) => setOpponentAvgPointsAllowed(e.target.value)} placeholder="Opponent Avg Points Allowed" required />
                <button type="submit">Predict Points</button>
            </form>
            {predictedPoints !== null && <div>Predicted Points: {predictedPoints}</div>}
        </div>
    );
};

export default Dashboard;
