import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.gameover}>
      <div className={styles.rectangle77} />
      <div className={styles.rectangle78} />
      <p className={styles.gAmeover}>
        GAME <br />
        &nbsp;&nbsp;&nbsp;OVER
      </p>
      <div className={styles.rectangle73} />
      <img src="../image/moirlr3y-2tnrccv.svg" className={styles.frame} />
      <img src="../image/moirlr3z-0s84n8b.svg" className={styles.frame2} />
      <img src="../image/moirlr40-qhbfmd3.png" className={styles.rectangle} />
      <img src="../image/moirlr3z-4hn1fip.svg" className={styles.maskGroup} />
      <div className={styles.frame3}>
        <div className={styles.rectangle76} />
        <p className={styles.text}>最终得分：</p>
      </div>
    </div>
  );
}

export default Component;
