import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.frame2}>
      <div className={styles.frame}>
        <div className={styles.vector24}>
          <p className={styles.text}>
            我只是实验BOSS，很多武器
            <br />
            还没研发完成，别太得意了！
          </p>
          <img src="../image/mohwmsde-w1kbg10.svg" className={styles.group43} />
        </div>
      </div>
      <img src="../image/mohwmsde-wf7rsum.png" className={styles.maskGroup} />
    </div>
  );
}

export default Component;
