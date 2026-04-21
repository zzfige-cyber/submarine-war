import React from 'react';

import styles from './index.module.scss';

const Component = () => {
  return (
    <div className={styles.frame}>
      <div className={styles.group14}>
        <img src="../image/mo5rcpii-6lg3jbs.png" className={styles.union} />
        <img src="../image/mo5rcpii-awskuqu.svg" className={styles.rectangle8} />
        <div className={styles.rectangle7}>
          <p className={styles.text}>涡轮增压</p>
          <p className={styles.text2}>每升1级+10%的移速</p>
        </div>
        <div className={styles.rectangle9}>
          <p className={styles.text3}>装甲厚度</p>
          <p className={styles.text4}>每升1级+最大血量20%</p>
        </div>
        <div className={styles.rectangle10}>
          <p className={styles.text5}>弹药库</p>
          <p className={styles.text6}>每升1级弹药库容量+20%</p>
        </div>
        <p className={styles.text7}>剩余技能点：</p>
      </div>
      <p className={styles.skIllcongiguration}>SkILL CONGIGURATION</p>
    </div>
  );
}

export default Component;
